function [E_z,state_vector]=MouseMovement_2D_TEM(obj,dontknow,f,h,kind,full)
    %Gets called upon Mousemovement 
    if nargin==5
        full=0;
    end
        
    %Lade Parameter
    [d,a,eps_1,eps_2,n_max,plot_how_many,how_fine,ax1,axh1,axh2,axh3,axh4,plot_before,K,k_x,k_y,q,n,G,n_10]=appdata_load(f,'d','a','eps_1','eps_2','n_max','plot_how_many','how_fine','ax1','axh1','axh2','axh3','axh4','plot_before','K','k_x','k_y','q','n','G_mat','n_10');
    %Bestimme Mausposition in Axis
    [pos inside]=Pix2Pos(f,ax1);
    if inside==1
        set(f,'Pointer','crosshair');
    else
        set(f,'Pointer','arrow');
    end
    if full==0
        n_max=10;
        
        if n_10==0
            area=a^2*sqrt(3);
            pw=(2*n_max+1)^2;
            b1=2*pi/a*(1-sqrt(3)/3*1i);                  %Primitie reciprocal lattice   -> real part is         x-axis    
            b2=2*pi/a*2*sqrt(3)/3*1i;                    %Primitie reciprocal lattice   -> imaginary part is    y-axis
            %Create some empty matrizes to fill
            prefactor=2/area*pi*d;  %Prefactor for Fourier Transform
            K=ones(pw,pw)*prefactor*(eps_1-eps_2);  %K_list
            K_nq=zeros(pw,pw);
            G=zeros(pw,1);

            n=zeros(pw,1); %Index Positions in Matrizes of n
            q=zeros(pw,1); %Index Positions in Matrizes of q
            for i=1:pw
                 n(i)=floor(mod(i-1,pw)/(2*n_max+1))-n_max;
                 q(i)=mod(i-1,2*n_max+1)-n_max;
                 G(i)=n(i)*b1+q(i)*b2;
            end
            %Do the bulk of the calculation
            for i=1:pw
                for j=i+1:pw
                    K(i,j)=K(i,j)*besselj(1,d/2*abs(G(i)-G(j)))/abs(G(i)-G(j));
                    K(j,i)=K(i,j);          %Use symmetry :D I <3 Symmetry
                end
                K(i,i)=(1-prefactor*d/4)*eps_2+prefactor*eps_1*d/4;   %Add the constant background factor
            end
            K=inv(K);
            appdata_save(f,'n_1',n,'q_1',q,'K_1',K);
        else
            [n q K]=appdata_load(f,'n_1','q_1','K_1');
        end
    end
    if inside==1
        %% Determine the field distribution in space
        k_z=round(pos(1));  %Where we at?
        k_x=k_x(k_z);
        k_y=k_y(k_z);
        k=k_x+1i*k_y;
        
        pw=(2*n_max+1)^2;
        K_nq=zeros(pw,pw);
        %Generate K_nq
        for l=1:(2*n_max+1)^2   %Vector components of field representing fourier components
            for m=1:(2*n_max+1)^2   %q and n components
                alpha=2*pi/(sqrt(3)*a)*(2*q(m)-n(m))+k_y;
                beta=2*pi/a*n(m)+k_x;
                if kind=='TE'
                    K_nq(l,m)=K(l,m)*(alpha^2+beta^2);
                else
                    K_nq(l+(2*n_max+1)^2*[0 1],m+(2*n_max+1)^2*[0 1])=K(l,m)*[alpha^2       -alpha*beta;...
                                                                              -alpha*beta   beta^2];
                end
            end
        end
        %Determine eigenvalues via 
        [V,D]=eig(K_nq);
        omega=diag(D);
        [omega_k indexes]=sort(sqrt(omega));   
        %Search for minimal distance to mouse
        [mini mindex]=min(abs(pos(2)-omega_k));
        omega=omega_k(mindex);
        %coloumnist=indexes(mindex);
        state_vector=V(:,indexes(mindex));  %This is the state vector 
        %% Plot circle|point in f
        if plot_before==1
            delete(appdata_load(f,'point_plot'));
        end
        hold(ax1,'on');
        limx=get(ax1,'xlim');
        limy=get(ax1,'ylim');
        point_plot=plot(ax1,k_z,omega,'ok');
        hold(ax1,'off');
        set(ax1,'xlim',limx);
        set(ax1,'ylim',limy);
        appdata_save(f,'plot_before',1,'point_plot',point_plot);
        
        %% Calculate the field distribution
        detail=2*n_max+1;
        if full==1
            detail=detail*10;
        end
        E_z=zeros(detail,detail);
        [x,y]=meshgrid(linspace(-a,a,detail)/2,linspace(-sqrt(3)*a,sqrt(3)*a,detail)/2);
        prematrix=exp(-1i*(k_x*x+k_y*y));
        if kind=='TE'
            for i=1:length(state_vector)
                E_z=E_z+state_vector(i)*exp(-1i*(2*pi*n(i)/a*x+2*pi/(sqrt(3)*a)*(2*q(i)-n(i))*y));
            end
        else
            for i=1:length(state_vector)/2
                E_z=E_z+state_vector(i)*exp(-1i*(2*pi*n(i)/a*x+2*pi/(sqrt(3)*a)*(2*q(i)-n(i))*y))*state_vector(i+length(state_vector)/2);
            end
        end
        E_z=E_z.*prematrix;
        %Same direction
        if E_z(1)>E_z(2)
            E_z=-E_z;
        end
        %Normalization
        I=sum(sum(abs(E_z).^2));
        E_z=E_z/I;
        
        %% Plot the field distribution
        set(0,'CurrentFigure',h);
        set(h,'Name',['TE Field of Hole Structure: ' 'w/c=' num2str(omega) ' k_x=' num2str(k_x) ' k_y' num2str(k_y)]);
        axh=[axh1 axh2 axh3];
        titles={'Absolute Field','Real Field','Imaginary Field'};
        color_limits=[min([abs(E_z(:));real(E_z(:));imag(E_z(:))]) max([abs(E_z(:));real(E_z(:));imag(E_z(:))])];
        for i=1:3
            axes(axh(i))
            if i==1
                imagesc([-a/2 a/2],sqrt(3)*a*[-1/2 1/2],abs(E_z),color_limits)
            elseif i==2
                imagesc([-a/2 a/2],sqrt(3)*a*[-1/2 1/2],real(E_z),color_limits)
            else
                imagesc([-a/2 a/2],sqrt(3)*a*[-1/2 1/2],imag(E_z),color_limits) 
            end
            %Background
            %Holes
            hold on;
            rectangle('Position',[-d/2 -d/2 d d],'Curvature',[1 1],'FaceColor','none','LineStyle','-','EdgeColor','r');
            rectangle('Position',[-d/2-a/2 -d/2-a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','none','LineStyle','-','EdgeColor','r');
            rectangle('Position',[-d/2+a/2 -d/2-a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','none','LineStyle','-','EdgeColor','r');
            rectangle('Position',[-d/2-a/2 -d/2+a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','none','LineStyle','-','EdgeColor','r');
            rectangle('Position',[-d/2+a/2 -d/2+a*sqrt(3)/2 d d],'Curvature',[1 1],'FaceColor','none','LineStyle','-','EdgeColor','r');
            %text(0,0,['\epsilon_2=' num2str(eps_2,'	%u')],'Color','white','HorizontalAlignment','center')
            %text(d/2,d/2,['\epsilon_1=' num2str(eps_1,'	%u')],'Color','black','HorizontalAlignment','center')
            hold off;

            axis(a/2*[-1 1 -sqrt(3) sqrt(3)])
            xlabel('x')
            ylabel('y')
            xlabel('x')
            ylabel('y')
            axis([-1,1,-sqrt(3),sqrt(3)]*a/2)
            title(titles{i});
        end
        axes(axh4)
        caxis(color_limits);
        colorbar('location','west')
        set(0,'CurrentFigure',f);
    end
end